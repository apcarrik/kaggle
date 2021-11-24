def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[10]<=2:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[16]<=3.0:
				return 'False'
			elif obj[16]>3.0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[8]<=1:
				return 'True'
			elif obj[8]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]>2:
		return 'True'
	else: return 'True'
