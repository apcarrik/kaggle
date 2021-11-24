def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[17]<=2:
		# {"feature": "Restaurantlessthan20", "instances": 43, "metric_value": 0.9965, "depth": 2}
		if obj[14]<=2.0:
			# {"feature": "Passanger", "instances": 25, "metric_value": 0.8555, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Weather", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[11]<=4:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[3]>1:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[6]<=4:
								return 'False'
							elif obj[6]>4:
								return 'True'
							else: return 'True'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					elif obj[11]>4:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[14]>2.0:
			# {"feature": "Time", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[4]>0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[17]>2:
		return 'False'
	else: return 'False'
