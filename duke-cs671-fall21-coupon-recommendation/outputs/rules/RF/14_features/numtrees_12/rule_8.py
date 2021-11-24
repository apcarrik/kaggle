def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[2]>1:
		# {"feature": "Income", "instances": 60, "metric_value": 0.9007, "depth": 2}
		if obj[8]>1:
			# {"feature": "Time", "instances": 48, "metric_value": 0.7766, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[7]<=9:
					# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[11]<=3.0:
						# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.6723, "depth": 6}
						if obj[10]<=1.0:
							# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[3]>0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[9]<=0.0:
										# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6]<=0:
												return 'True'
											elif obj[6]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>0.0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>4:
								return 'False'
							else: return 'False'
						elif obj[10]>1.0:
							return 'True'
						else: return 'True'
					elif obj[11]>3.0:
						return 'False'
					else: return 'False'
				elif obj[7]>9:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]>0:
						# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]>3:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.4262, "depth": 4}
				if obj[11]>-1.0:
					# {"feature": "Age", "instances": 22, "metric_value": 0.2668, "depth": 5}
					if obj[4]>0:
						return 'True'
					elif obj[4]<=0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]<=-1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=1:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[7]>5:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[10]<=2.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>2:
							return 'False'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[10]>2.0:
					return 'True'
				else: return 'True'
			elif obj[7]<=5:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Income", "instances": 25, "metric_value": 0.795, "depth": 2}
		if obj[8]<=5:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>5:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[4]>1:
					return 'True'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
