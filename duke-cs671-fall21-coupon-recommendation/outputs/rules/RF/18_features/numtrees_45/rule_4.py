def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[14]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[3]>2:
		# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[0]>0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[10]<=5:
						return 'True'
					elif obj[10]>5:
						return 'False'
					else: return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
