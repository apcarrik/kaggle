def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[2]>0:
		# {"feature": "Education", "instances": 73, "metric_value": 0.9693, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Coffeehouse", "instances": 69, "metric_value": 0.9816, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Occupation", "instances": 53, "metric_value": 0.9414, "depth": 4}
				if obj[7]<=10:
					# {"feature": "Age", "instances": 36, "metric_value": 0.8524, "depth": 5}
					if obj[4]>0:
						# {"feature": "Time", "instances": 32, "metric_value": 0.7579, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Children", "instances": 24, "metric_value": 0.5436, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.6962, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]>0.0:
											return 'True'
										elif obj[8]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0]>1:
										return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]<=0.0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>0.0:
									return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=0:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[11]<=0:
							return 'False'
						elif obj[11]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>10:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[12]<=1:
						# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[4]>0:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[8]<=3.0:
								return 'False'
							elif obj[8]>3.0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[12]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]<=0.0:
				# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[1]>0:
					# {"feature": "Age", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]>1:
								return 'False'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>4:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[10]<=1.0:
							return 'False'
						elif obj[10]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[7]<=6:
			return 'False'
		elif obj[7]>6:
			# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]<=2:
				return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
