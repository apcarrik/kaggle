def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 170, "metric_value": 0.9999, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon_validity", "instances": 122, "metric_value": 0.9805, "depth": 2}
		if obj[6]>0:
			# {"feature": "Education", "instances": 63, "metric_value": 0.9911, "depth": 3}
			if obj[11]>1:
				# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9082, "depth": 4}
				if obj[18]>0.0:
					# {"feature": "Gender", "instances": 27, "metric_value": 0.9751, "depth": 5}
					if obj[7]>0:
						# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9887, "depth": 6}
						if obj[15]>0.0:
							# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[4]<=1:
									# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[2]<=0:
										return 'True'
									elif obj[2]>0:
										return 'False'
									else: return 'False'
								elif obj[4]>1:
									return 'False'
								else: return 'False'
							elif obj[9]>0:
								return 'True'
							else: return 'True'
						elif obj[15]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[7]<=0:
						# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[17]<=3.0:
							return 'False'
						elif obj[17]>3.0:
							# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=0:
								return 'True'
							elif obj[0]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[18]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[11]<=1:
				# {"feature": "Temperature", "instances": 29, "metric_value": 0.9784, "depth": 4}
				if obj[3]>55:
					# {"feature": "Income", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[13]<=4:
						# {"feature": "Driving_to", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[14]<=1.0:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[4]<=1:
										return 'False'
									elif obj[4]>1:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							elif obj[14]>1.0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[13]>4:
						return 'True'
					else: return 'True'
				elif obj[3]<=55:
					# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=4:
						return 'True'
					elif obj[8]>4:
						# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[13]>3:
							return 'False'
						elif obj[13]<=3:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[6]<=0:
			# {"feature": "Bar", "instances": 59, "metric_value": 0.8432, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Driving_to", "instances": 54, "metric_value": 0.7642, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 44, "metric_value": 0.8454, "depth": 5}
					if obj[4]>1:
						# {"feature": "Occupation", "instances": 31, "metric_value": 0.6374, "depth": 6}
						if obj[12]>5:
							# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.8315, "depth": 7}
							if obj[15]<=1.0:
								# {"feature": "Carryaway", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[16]<=2.0:
									# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[8]<=4:
											return 'True'
										elif obj[8]>4:
											# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1]>2:
												return 'True'
											elif obj[1]<=2:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>1:
										return 'False'
									else: return 'False'
								elif obj[16]>2.0:
									return 'False'
								else: return 'False'
							elif obj[15]>1.0:
								return 'True'
							else: return 'True'
						elif obj[12]<=5:
							return 'True'
						else: return 'True'
					elif obj[4]<=1:
						# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[8]>1:
							# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[12]>3:
									# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]<=55:
										return 'True'
									elif obj[3]>55:
										return 'False'
									else: return 'False'
								elif obj[12]<=3:
									return 'False'
								else: return 'False'
							elif obj[11]>0:
								return 'True'
							else: return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[14]>2.0:
				# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Bar", "instances": 48, "metric_value": 0.8427, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[17]<=2.0:
					# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[8]<=4:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[12]<=19:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[15]>0.0:
								return 'False'
							elif obj[15]<=0.0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]>0:
										return 'True'
									elif obj[11]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[12]>19:
							return 'True'
						else: return 'True'
					elif obj[8]>4:
						return 'True'
					else: return 'True'
				elif obj[17]>2.0:
					return 'True'
				else: return 'True'
			elif obj[6]>0:
				# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[13]<=4:
					return 'False'
				elif obj[13]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[14]<=0.0:
			# {"feature": "Age", "instances": 24, "metric_value": 0.4138, "depth": 3}
			if obj[8]<=4:
				return 'False'
			elif obj[8]>4:
				# {"feature": "Carryaway", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[16]>1.0:
					# {"feature": "Driving_to", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[10]<=0:
							return 'True'
						elif obj[10]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[16]<=1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	else: return 'False'
