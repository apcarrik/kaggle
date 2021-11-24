def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Children", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[9]<=0:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[4]>0:
			# {"feature": "Income", "instances": 24, "metric_value": 0.8113, "depth": 3}
			if obj[12]>3:
				# {"feature": "Bar", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[13]<=2.0:
					# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=4:
						return 'True'
					elif obj[7]>4:
						# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>55:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=55:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[13]>2.0:
					return 'False'
				else: return 'False'
			elif obj[12]<=3:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[9]>0:
		# {"feature": "Passanger", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[0]>1:
			# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[3]>2:
				# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=2:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
