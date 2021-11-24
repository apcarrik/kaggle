def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Income", "instances": 61, "metric_value": 0.8949, "depth": 2}
		if obj[8]>0:
			# {"feature": "Education", "instances": 54, "metric_value": 0.9357, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Passanger", "instances": 43, "metric_value": 0.9808, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 27, "metric_value": 0.9911, "depth": 5}
					if obj[7]<=9:
						# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 6}
						if obj[13]<=2:
							# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[4]>2:
								# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[12]<=0:
										# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9]<=0.0:
											return 'False'
										elif obj[9]>0.0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[11]<=0.0:
												return 'False'
											elif obj[11]>0.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[12]>0:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						elif obj[13]>2:
							return 'True'
						else: return 'True'
					elif obj[7]>9:
						# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[10]<=3.0:
						# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 6}
						if obj[7]>4:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]>0:
										return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						elif obj[7]<=4:
							return 'True'
						else: return 'True'
					elif obj[10]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=0:
						return 'True'
					elif obj[3]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[8]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Gender", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[3]>0:
				return 'False'
			elif obj[3]<=0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>1.0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[7]>1:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[13]<=2:
					return 'True'
				elif obj[13]>2:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>2:
							return 'True'
						elif obj[6]<=2:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[7]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
