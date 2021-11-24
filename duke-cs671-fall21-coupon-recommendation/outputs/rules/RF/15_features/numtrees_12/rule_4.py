def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Distance", "instances": 55, "metric_value": 0.971, "depth": 2}
		if obj[14]<=1:
			# {"feature": "Income", "instances": 28, "metric_value": 0.9852, "depth": 3}
			if obj[9]>1:
				# {"feature": "Time", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[1]>0:
					# {"feature": "Children", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[2]>1:
							# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[8]<=7:
								# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=2.0:
									# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[10]>0.0:
										return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]>3:
											return 'False'
										elif obj[5]<=3:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[11]>2.0:
									return 'False'
								else: return 'False'
							elif obj[8]>7:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]<=1:
				return 'False'
			else: return 'False'
		elif obj[14]>1:
			# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.7642, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Occupation", "instances": 26, "metric_value": 0.7063, "depth": 4}
				if obj[8]<=13:
					# {"feature": "Children", "instances": 21, "metric_value": 0.7919, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[7]>1:
								# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[9]>0:
									return 'False'
								elif obj[9]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>0:
						# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[9]>1:
							# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>1:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>1:
									return 'True'
								elif obj[1]<=1:
									return 'False'
								else: return 'False'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[9]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[8]>13:
					return 'False'
				else: return 'False'
			elif obj[12]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.8366, "depth": 2}
		if obj[2]>0:
			# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.7496, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Bar", "instances": 26, "metric_value": 0.6194, "depth": 4}
				if obj[10]<=0.0:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[8]<=8:
						# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[7]<=2:
							return 'True'
						elif obj[7]>2:
							# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[11]>2.0:
								return 'True'
							elif obj[11]<=2.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>8:
						return 'False'
					else: return 'False'
				elif obj[10]>0.0:
					return 'True'
				else: return 'True'
			elif obj[12]>2.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
