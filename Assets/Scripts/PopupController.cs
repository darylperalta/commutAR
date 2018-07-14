using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PopupController : MonoBehaviour {

	public GameObject destination;
	public int target;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		transform.GetChild(0).gameObject.SetActive(destination.transform.parent.GetSiblingIndex() == target);
		transform.GetChild(1).gameObject.SetActive(destination.transform.parent.GetSiblingIndex() == target);
	}
}
