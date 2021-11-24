def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 90, "metric_value": 0.8813, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Passanger", "instances": 72, "metric_value": 0.7383, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Income", "instances": 49, "metric_value": 0.8631, "depth": 4}
				if obj[8]<=7:
					# {"feature": "Age", "instances": 43, "metric_value": 0.9103, "depth": 5}
					if obj[4]>1:
						# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.9673, "depth": 6}
						if obj[11]>0.0:
							# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.8936, "depth": 7}
							if obj[10]>1.0:
								# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[7]>6:
											return 'False'
										elif obj[7]<=6:
											# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[1]>2:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[9]<=0.0:
									# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[7]>2:
										return 'True'
									elif obj[7]<=2:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]>1:
											return 'True'
										elif obj[1]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[10]<=1.0:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[13]<=2:
									return 'True'
								elif obj[13]>2:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[11]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[4]<=1:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[7]<=20:
							return 'True'
						elif obj[7]>20:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]>7:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.258, "depth": 4}
				if obj[7]<=10:
					return 'True'
				elif obj[7]>10:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Passanger", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Gender", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]>6:
						return 'False'
					elif obj[7]<=6:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[8]<=5:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[11]>0.0:
						return 'False'
					elif obj[11]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[8]>5:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Income", "instances": 37, "metric_value": 0.878, "depth": 2}
		if obj[8]<=4:
			# {"feature": "Bar", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[7]<=9:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Gender", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[3]>0:
							# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[1]>1:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]<=0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[11]<=1.0:
											return 'True'
										elif obj[11]>1.0:
											return 'False'
										else: return 'False'
									elif obj[4]>0:
										return 'True'
									else: return 'True'
								elif obj[0]>0:
									return 'False'
								else: return 'False'
							elif obj[1]<=1:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[10]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[7]>9:
					return 'True'
				else: return 'True'
			elif obj[9]<=0.0:
				# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[11]<=2.0:
					return 'False'
				elif obj[11]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>4:
			# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[4]<=5:
				return 'False'
			elif obj[4]>5:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
