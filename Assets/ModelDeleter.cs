using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ModelDeleter : MonoBehaviour {

	public GameObject parent;
	public GameObject panel;

	public void delete() {
		Destroy(parent.transform.GetChild(0).gameObject);
		panel.GetComponent<Canvas>().enabled = false;
	}

}
