def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Driving_to", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Distance", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[19]>1:
			# {"feature": "Children", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Temperature", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[3]<=55:
					# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[16]<=3.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[16]>3.0:
						return 'False'
					else: return 'False'
				elif obj[3]>55:
					return 'False'
				else: return 'False'
			elif obj[10]>0:
				return 'False'
			else: return 'False'
		elif obj[19]<=1:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[12]<=10:
				# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[13]<=6:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[15]<=1.0:
							# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[16]>0.0:
								return 'False'
							elif obj[16]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[15]>1.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[13]>6:
					return 'True'
				else: return 'True'
			elif obj[12]>10:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Income", "instances": 22, "metric_value": 0.7732, "depth": 2}
		if obj[13]>3:
			return 'True'
		elif obj[13]<=3:
			# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[12]<=7:
				# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[9]>0:
					return 'True'
				elif obj[9]<=0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=3:
						return 'False'
					elif obj[4]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]>7:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
