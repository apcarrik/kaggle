def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]>1:
		# {"feature": "Age", "instances": 26, "metric_value": 0.9306, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Time", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[13]<=2.0:
					return 'True'
				elif obj[13]>2.0:
					return 'False'
				else: return 'False'
			elif obj[2]>2:
				# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[11]<=3:
					return 'False'
				elif obj[11]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>3:
			# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[7]<=1:
				return 'True'
			elif obj[7]>1:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		return 'False'
	else: return 'False'
