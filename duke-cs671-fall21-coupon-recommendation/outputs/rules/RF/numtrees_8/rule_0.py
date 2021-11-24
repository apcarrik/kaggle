def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Distance", "instances": 92, "metric_value": 0.9969, "depth": 2}
		if obj[20]>1:
			# {"feature": "Temperature", "instances": 49, "metric_value": 0.9113, "depth": 3}
			if obj[3]>30:
				# {"feature": "Occupation", "instances": 32, "metric_value": 0.6962, "depth": 4}
				if obj[12]<=6:
					# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[15]>1.0:
						# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[13]>2:
							# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Driving_to", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[13]<=2:
							return 'False'
						else: return 'False'
					elif obj[15]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[12]>6:
					return 'False'
				else: return 'False'
			elif obj[3]<=30:
				# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[8]>1:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[5]<=3:
						return 'True'
					elif obj[5]>3:
						return 'False'
					else: return 'False'
				elif obj[8]<=1:
					# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[20]<=1:
			# {"feature": "Carryaway", "instances": 43, "metric_value": 0.9523, "depth": 3}
			if obj[16]>1.0:
				# {"feature": "Restaurantlessthan20", "instances": 37, "metric_value": 0.878, "depth": 4}
				if obj[17]>2.0:
					# {"feature": "Coupon_validity", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[4]<=2:
							return 'True'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					elif obj[6]>0:
						# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]>0:
								return 'True'
							elif obj[9]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[17]<=2.0:
					# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.5033, "depth": 5}
					if obj[15]<=3.0:
						# {"feature": "Coupon", "instances": 17, "metric_value": 0.3228, "depth": 6}
						if obj[5]>0:
							return 'True'
						elif obj[5]<=0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=1:
								return 'True'
							elif obj[8]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[15]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[16]<=1.0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]<=2:
					return 'False'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Restaurantlessthan20", "instances": 35, "metric_value": 0.8224, "depth": 2}
		if obj[17]<=3.0:
			# {"feature": "Age", "instances": 33, "metric_value": 0.7455, "depth": 3}
			if obj[8]<=5:
				# {"feature": "Time", "instances": 24, "metric_value": 0.4138, "depth": 4}
				if obj[4]<=3:
					return 'True'
				elif obj[4]>3:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[5]<=3:
						return 'True'
					elif obj[5]>3:
						# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]>0:
							return 'False'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[8]>5:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[14]<=0.0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=1:
						return 'False'
					elif obj[5]>1:
						# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=0:
							return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[14]>0.0:
					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[10]>0:
						return 'True'
					elif obj[10]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[17]>3.0:
			return 'False'
		else: return 'False'
	else: return 'True'
