def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[13]<=3.0:
		# {"feature": "Maritalstatus", "instances": 27, "metric_value": 0.8767, "depth": 2}
		if obj[7]<=1:
			# {"feature": "Time", "instances": 20, "metric_value": 0.469, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[11]<=2:
					return 'False'
				elif obj[11]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>1:
			# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=1:
				return 'True'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[13]>3.0:
		return 'True'
	else: return 'True'
