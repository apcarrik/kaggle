def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[4]>1:
		# {"feature": "Coupon_validity", "instances": 93, "metric_value": 0.9554, "depth": 2}
		if obj[5]>0:
			# {"feature": "Bar", "instances": 49, "metric_value": 0.9997, "depth": 3}
			if obj[13]<=1.0:
				# {"feature": "Age", "instances": 36, "metric_value": 0.9641, "depth": 4}
				if obj[7]<=3:
					# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[10]>0:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[16]<=1.0:
							# {"feature": "Coffeehouse", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[14]<=3.0:
								# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[2]>55:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]>1:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6]<=0:
												return 'False'
											elif obj[6]>0:
												return 'True'
											else: return 'True'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[2]<=55:
										return 'True'
									else: return 'True'
								elif obj[9]>0:
									return 'False'
								else: return 'False'
							elif obj[14]>3.0:
								return 'True'
							else: return 'True'
						elif obj[16]>1.0:
							return 'True'
						else: return 'True'
					elif obj[10]<=0:
						return 'False'
					else: return 'False'
				elif obj[7]>3:
					# {"feature": "Education", "instances": 17, "metric_value": 0.6723, "depth": 5}
					if obj[10]<=1:
						return 'True'
					elif obj[10]>1:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[11]<=5:
							return 'False'
						elif obj[11]>5:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[13]>1.0:
				# {"feature": "Time", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=4:
						return 'True'
					elif obj[7]>4:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Passanger", "instances": 44, "metric_value": 0.7732, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.9059, "depth": 4}
				if obj[14]<=3.0:
					# {"feature": "Income", "instances": 23, "metric_value": 0.9656, "depth": 5}
					if obj[12]<=5:
						# {"feature": "Time", "instances": 19, "metric_value": 0.8315, "depth": 6}
						if obj[3]>0:
							# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[7]>2:
									return 'False'
								elif obj[7]<=2:
									# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[2]<=55:
										return 'True'
									elif obj[2]>55:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]>2:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[12]>5:
						return 'False'
					else: return 'False'
				elif obj[14]>3.0:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[18]>1:
					return 'True'
				elif obj[18]<=1:
					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>30:
						return 'True'
					elif obj[2]<=30:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Income", "instances": 34, "metric_value": 0.9597, "depth": 2}
		if obj[12]>3:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.7025, "depth": 3}
			if obj[16]<=1.0:
				return 'False'
			elif obj[16]>1.0:
				# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[12]<=3:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[18]>1:
					return 'False'
				elif obj[18]<=1:
					return 'True'
				else: return 'True'
			elif obj[14]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
