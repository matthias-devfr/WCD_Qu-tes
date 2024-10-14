/*********************************************************************************
 *
 * Ce fichier contient toutes les fonctions nécessaires au fonctionnement du jeu.
 *
 *********************************************************************************/

/**
 * Cette fonction affiche dans la console le score de l'utilisateur
 * @param {number} score : le score de l'utilisateur
 * @param {number} nbMotsProposes : le nombre de mots proposés à l'utilisateur
 */
function afficherResultat(score, nbMotsProposes) {
  // Récupération de la zone dans laquelle on va écrire le score
  let spanScore = document.querySelector(".zoneScore span")
  // Ecriture du texte
  let affichageScore = `${score} / ${nbMotsProposes}`
  // On place le texte à l'intérieur du span.
  spanScore.innerText = affichageScore
}

/**
 * Cette fonction affiche une proposition, que le joueur devra recopier,
 * dans la zone "zoneProposition"
 * @param {string} proposition : la proposition à afficher
 */
function afficherProposition(proposition) {
  let zoneProposition = document.querySelector(".zoneProposition")
  zoneProposition.innerText = proposition
}

/**
 * Cette fonction construit et affiche l'email.
 * @param {string} nom : le nom du joueur
 * @param {string} email : l'email de la personne avec qui il veut partager son score
 * @param {string} score : le score.
 */
function afficherEmail(nom, email, score) {
  let mailto = `mailto:${email}?subject=Partage du score Azertype&body=Salut, je suis ${nom} et je viens de réaliser le score ${score} sur le site d'Azertype !`
  location.href = mailto
}

function validerNom(nom) {
  if (nom.length >= 2) {
    return true
  }
  return false
}

function validerEmail(email) {
  let emailRegExp = new RegExp("[a-z0-9.-_]+@[a-z0-9.-_]+\\.[a-z0-9.-_]+")
  if (emailRegExp.test(email)) {
    return true
  }
  return false
}

/**
 * Cette fonction lance le jeu.
 * Elle demande à l'utilisateur de choisir entre "mots" et "phrases" et lance la boucle de jeu correspondante
 */
function lancerJeu() {
  // Initialisations
  initAddEventListenerPopup()
  let score = 0
  let i = 0
  let listeProposition = listeMots

  let btnValiderMot = document.getElementById("btnValiderMot")
  let inputEcriture = document.getElementById("inputEcriture")

  afficherProposition(listeProposition[i])

  // Gestion de l'événement click sur le bouton "valider"
  btnValiderMot.addEventListener("click", () => {
    // Vérifie si le jeu n'est pas terminé et si la réponse a au moins 6 caractères
    if (listeProposition[i] !== undefined) {
      if (inputEcriture.value.trim().length >= 6) {
        if (inputEcriture.value === listeProposition[i]) {
          score++
        }
        i++
        afficherResultat(score, i)
        inputEcriture.value = ""
        if (listeProposition[i] === undefined) {
          afficherProposition("Le jeu est fini")
          btnValiderMot.disabled = true
        } else {
          afficherProposition(listeProposition[i])
        }
      } else {
        // Alert lorsque la longueur de la réponse est incorrecte
        alert("OUPS !! Votre réponse est incorrecte ! Verifiez votre réponse avant de valider ;-)")
      }
    }
  })
  // Gestion de l'événement "keypress" sur la zone de saisie
  inputEcriture.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
      event.preventDefault() // Empêche le comportement par défaut de la touche "Entrée"

      // Vérifie si le jeu n'est pas terminé et si la réponse a au moins 6 caractères
      if (listeProposition[i] !== undefined && inputEcriture.value.trim().length >= 6) {
        if (inputEcriture.value === listeProposition[i]) {
          score++
        }
        i++
        afficherResultat(score, i)
        inputEcriture.value = ""
        if (listeProposition[i] === undefined) {
          afficherProposition("Le jeu est fini")
          btnValiderMot.disabled = true
        } else {
          afficherProposition(listeProposition[i])
        }
      } else {
        // Alert lorsque la longueur de la réponse est incorrecte
        alert("OUPS !! Votre réponse est incorrecte ! Verifiez votre réponse avant de valider ;-)")
      }
    }
  })

  // Gestion de l'événement change sur les boutons radios.
  let listeBtnRadio = document.querySelectorAll(".optionSource input")
  for (let index = 0; index < listeBtnRadio.length; index++) {
    listeBtnRadio[index].addEventListener("change", (event) => {
      // Si c'est le premier élément qui a été modifié, alors nous voulons
      // jouer avec la listeMots.
      if (event.target.value === "1") {
        listeProposition = listeMots
      } else {
        // Sinon nous voulons jouer avec la liste des phrases
        listeProposition = listePhrases
      }
      // Et on modifie l'affichage en direct.
      afficherProposition(listeProposition[i])
    })
  }

  let form = document.querySelector("form")
  form.addEventListener("submit", (Event) => {
    Event.preventDefault()

    let baliseNom = document.getElementById("nom")
    let nom = baliseNom.value

    let baliseEmail = document.getElementById("email")
    let email = baliseEmail.value
    console.log(nom, email)

    if (validerNom(nom) && validerEmail(email)) {
      let scoreEmail = `${score} / ${i}`
      afficherEmail(nom, email, scoreEmail)
    } else {
      console.log("erreur de saisie")
    }
  })

  afficherResultat(score, i)
}
