def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.987, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 92, "metric_value": 0.9109, "depth": 2}
		if obj[7]>1.0:
			# {"feature": "Time", "instances": 50, "metric_value": 0.6801, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Age", "instances": 38, "metric_value": 0.7897, "depth": 4}
				if obj[3]<=4:
					# {"feature": "Distance", "instances": 30, "metric_value": 0.8813, "depth": 5}
					if obj[10]<=1:
						# {"feature": "Occupation", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[5]<=11:
							return 'True'
						elif obj[5]>11:
							# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[6]>1.0:
								return 'False'
							elif obj[6]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]>1:
						# {"feature": "Education", "instances": 12, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[8]>-1.0:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[9]<=0:
									return 'True'
								elif obj[9]>0:
									return 'False'
								else: return 'False'
							elif obj[8]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>4:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[7]<=1.0:
			# {"feature": "Age", "instances": 42, "metric_value": 1.0, "depth": 3}
			if obj[3]>0:
				# {"feature": "Time", "instances": 32, "metric_value": 0.9745, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 23, "metric_value": 0.8865, "depth": 5}
					if obj[10]<=2:
						# {"feature": "Bar", "instances": 20, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=11:
								# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[0]>0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[8]<=0.0:
												return 'True'
											elif obj[8]>0.0:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]>2:
									return 'True'
								else: return 'True'
							elif obj[5]>11:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					elif obj[10]>2:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=6:
							return 'False'
						elif obj[5]>6:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[10]<=1:
						# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=20:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>1:
									return 'True'
								elif obj[0]<=1:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]>0.0:
										return 'True'
									elif obj[6]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]>20:
								return 'False'
							else: return 'False'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					elif obj[10]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]<=0:
				# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[5]>6:
						return 'False'
					elif obj[5]<=6:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[8]<=2.0:
			# {"feature": "Bar", "instances": 33, "metric_value": 0.799, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Time", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[5]<=12:
							# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]>2.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=2:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											return 'False'
										else: return 'False'
									elif obj[7]<=2.0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>4:
								return 'False'
							else: return 'False'
						elif obj[5]>12:
							return 'True'
						else: return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[6]<=0.0:
				# {"feature": "Age", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[3]<=5:
					return 'False'
				elif obj[3]>5:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
