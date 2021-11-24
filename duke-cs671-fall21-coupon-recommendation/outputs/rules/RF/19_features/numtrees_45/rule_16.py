def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Temperature", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=55:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[4]>2:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=1:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=0:
								return 'True'
							elif obj[10]>0:
								return 'False'
							else: return 'False'
						elif obj[3]>1:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[14]>1.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[4]<=2:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[10]<=2:
				return 'False'
			elif obj[10]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>55:
		return 'False'
	else: return 'False'
