def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[11]<=2.0:
		# {"feature": "Occupation", "instances": 75, "metric_value": 0.9988, "depth": 2}
		if obj[7]>0:
			# {"feature": "Passanger", "instances": 71, "metric_value": 0.9999, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coffeehouse", "instances": 49, "metric_value": 0.9755, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Direction_same", "instances": 27, "metric_value": 0.8256, "depth": 5}
					if obj[12]<=0:
						# {"feature": "Distance", "instances": 22, "metric_value": 0.684, "depth": 6}
						if obj[13]<=2:
							# {"feature": "Income", "instances": 19, "metric_value": 0.4855, "depth": 7}
							if obj[8]>0:
								# {"feature": "Age", "instances": 18, "metric_value": 0.3095, "depth": 8}
								if obj[4]<=4:
									return 'False'
								elif obj[4]>4:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6]<=1:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[6]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]<=0:
								return 'True'
							else: return 'True'
						elif obj[13]>2:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]>0:
						# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								return 'False'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[10]>1.0:
					# {"feature": "Bar", "instances": 22, "metric_value": 0.976, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[2]>0:
							# {"feature": "Income", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[8]>3:
								return 'True'
							elif obj[8]<=3:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[9]>1.0:
						# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[4]>1:
							return 'False'
						elif obj[4]<=1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>1:
								return 'True'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Children", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Income", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[8]<=4:
						return 'True'
					elif obj[8]>4:
						# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>1:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>0:
					# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=0:
			return 'True'
		else: return 'True'
	elif obj[11]>2.0:
		# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>2:
				return 'False'
			elif obj[0]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
