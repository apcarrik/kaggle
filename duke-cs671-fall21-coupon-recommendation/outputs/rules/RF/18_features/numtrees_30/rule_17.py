def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Age", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[6]>2:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[10]>5:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]<=5:
				return 'False'
			else: return 'False'
		elif obj[6]<=2:
			# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[9]<=3:
				return 'False'
			elif obj[9]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[14]<=3.0:
			return 'True'
		elif obj[14]>3.0:
			return 'False'
		else: return 'False'
	else: return 'True'
