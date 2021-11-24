def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[2]>0:
		# {"feature": "Education", "instances": 68, "metric_value": 0.9367, "depth": 2}
		if obj[6]>0:
			# {"feature": "Time", "instances": 44, "metric_value": 0.9985, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.9457, "depth": 4}
				if obj[7]<=9:
					# {"feature": "Income", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[8]>0:
						return 'False'
					elif obj[8]<=0:
						# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>9:
					# {"feature": "Children", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[13]<=2:
								return 'False'
							elif obj[13]>2:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[7]>1:
						# {"feature": "Income", "instances": 15, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=7:
							# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[0]>0:
										# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[10]>2.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[12]<=0:
													return 'True'
												elif obj[12]>0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[10]<=2.0:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]>3:
									return 'True'
								else: return 'True'
							elif obj[9]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[8]>7:
							return 'False'
						else: return 'False'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]<=0:
			# {"feature": "Age", "instances": 24, "metric_value": 0.5436, "depth": 3}
			if obj[4]>1:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=7:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[10]>0.0:
						return 'True'
					elif obj[10]<=0.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>7:
					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0:
						return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Direction_same", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[12]<=0:
			# {"feature": "Passanger", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]<=1:
					return 'True'
				elif obj[4]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[12]>0:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=2:
				return 'True'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
