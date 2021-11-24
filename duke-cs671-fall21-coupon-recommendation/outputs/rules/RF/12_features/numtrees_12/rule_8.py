def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Bar", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[7]<=2.0:
		# {"feature": "Time", "instances": 71, "metric_value": 0.9999, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 59, "metric_value": 0.9948, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Coupon", "instances": 54, "metric_value": 1.0, "depth": 4}
				if obj[2]>1:
					# {"feature": "Occupation", "instances": 35, "metric_value": 0.971, "depth": 5}
					if obj[6]<=7:
						# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.8555, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 7}
							if obj[11]<=1:
								# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[4]>2:
									return 'True'
								elif obj[4]<=2:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0]>0:
										# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=0:
												return 'True'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[11]>1:
								# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[5]<=2:
										return 'True'
									elif obj[5]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[8]>2.0:
							return 'True'
						else: return 'True'
					elif obj[6]>7:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[5]>1:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[11]<=1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]>2:
											return 'True'
										elif obj[4]<=2:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[11]>1:
									return 'False'
								else: return 'False'
							elif obj[5]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[6]>5:
						# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[0]>0:
							# {"feature": "Age", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[4]>1:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[11]>1:
												# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[11]<=2:
									return 'True'
								elif obj[11]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[6]<=5:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[9]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[6]>2:
				# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=2:
						return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[7]>2.0:
		# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[10]<=0:
			return 'True'
		elif obj[10]>0:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
