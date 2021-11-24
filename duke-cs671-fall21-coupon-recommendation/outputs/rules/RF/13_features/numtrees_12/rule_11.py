def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[1]>0:
		# {"feature": "Education", "instances": 62, "metric_value": 0.9629, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Coupon", "instances": 58, "metric_value": 0.9784, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Children", "instances": 33, "metric_value": 0.9993, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Age", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[4]<=6:
						# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 6}
						if obj[7]>1:
							# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[0]>1:
										return 'True'
									elif obj[0]<=1:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=0:
											return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[10]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[9]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[7]<=1:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1.0:
										return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>6:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[4]<=6:
							return 'False'
						elif obj[4]>6:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>2:
				# {"feature": "Distance", "instances": 25, "metric_value": 0.8555, "depth": 4}
				if obj[12]>1:
					# {"feature": "Gender", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>1:
									return 'True'
								elif obj[4]<=1:
									return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[7]>2:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=20:
							return 'False'
						elif obj[7]>20:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=1:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[8]<=2.0:
						return 'True'
					elif obj[8]>2.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Age", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[12]<=1:
					return 'False'
				elif obj[12]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[6]<=1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[7]<=14:
					return 'True'
				elif obj[7]>14:
					return 'False'
				else: return 'False'
			elif obj[6]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
