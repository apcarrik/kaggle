def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 15, "metric_value": 0.3534, "depth": 2}
		if obj[10]<=3:
			return 'False'
		elif obj[10]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[11]>1:
				return 'True'
			elif obj[11]<=1:
				return 'False'
			else: return 'False'
		elif obj[8]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
