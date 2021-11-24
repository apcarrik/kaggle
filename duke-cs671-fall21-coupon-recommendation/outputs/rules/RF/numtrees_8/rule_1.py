def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[5]>1:
		# {"feature": "Education", "instances": 96, "metric_value": 0.9464, "depth": 2}
		if obj[11]<=3:
			# {"feature": "Time", "instances": 85, "metric_value": 0.9774, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Age", "instances": 60, "metric_value": 0.9007, "depth": 4}
				if obj[8]>1:
					# {"feature": "Income", "instances": 35, "metric_value": 0.9852, "depth": 5}
					if obj[13]>1:
						# {"feature": "Distance", "instances": 28, "metric_value": 0.9059, "depth": 6}
						if obj[20]<=1:
							# {"feature": "Gender", "instances": 15, "metric_value": 0.5665, "depth": 7}
							if obj[7]>0:
								return 'True'
							elif obj[7]<=0:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[15]>0.0:
									# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[9]>0:
										return 'True'
									elif obj[9]<=0:
										# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[12]<=4:
											return 'False'
										elif obj[12]>4:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[15]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[20]>1:
							# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[14]<=1.0:
								# {"feature": "Driving_to", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=0:
									# {"feature": "Carryaway", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[16]<=2.0:
										# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9]<=0:
											return 'True'
										elif obj[9]>0:
											return 'False'
										else: return 'False'
									elif obj[16]>2.0:
										return 'False'
									else: return 'False'
								elif obj[0]>0:
									return 'True'
								else: return 'True'
							elif obj[14]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[13]<=1:
						# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[15]<=2.0:
							return 'False'
						elif obj[15]>2.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]<=1:
					# {"feature": "Restaurantlessthan20", "instances": 25, "metric_value": 0.6343, "depth": 5}
					if obj[17]<=2.0:
						# {"feature": "Carryaway", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[16]>1.0:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[12]>0:
								# {"feature": "Driving_to", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[0]>0:
									return 'True'
								elif obj[0]<=0:
									# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[3]<=55:
										return 'True'
									elif obj[3]>55:
										# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[13]>0:
											return 'False'
										elif obj[13]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[12]<=0:
								return 'False'
							else: return 'False'
						elif obj[16]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[17]>2.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>2:
				# {"feature": "Temperature", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[3]<=55:
					# {"feature": "Weather", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[2]>0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[12]<=12:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[15]<=2.0:
								return 'True'
							elif obj[15]>2.0:
								return 'False'
							else: return 'False'
						elif obj[12]>12:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>55:
					# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[8]<=3:
						return 'False'
					elif obj[8]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[11]>3:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Bar", "instances": 31, "metric_value": 0.8238, "depth": 2}
		if obj[14]>1.0:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[12]<=10:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[15]>1.0:
						# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>30:
							return 'True'
						elif obj[3]<=30:
							return 'False'
						else: return 'False'
					elif obj[15]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[12]>10:
				return 'False'
			else: return 'False'
		elif obj[14]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
