def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[9]>1.0:
		# {"feature": "Time", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.7219, "depth": 3}
			if obj[7]<=17:
				# {"feature": "Bar", "instances": 24, "metric_value": 0.65, "depth": 4}
				if obj[8]<=3.0:
					# {"feature": "Age", "instances": 23, "metric_value": 0.5586, "depth": 5}
					if obj[4]>1:
						# {"feature": "Passanger", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6]<=1:
										return 'True'
									elif obj[6]>1:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[11]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[8]>3.0:
					return 'False'
				else: return 'False'
			elif obj[7]>17:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[9]<=1.0:
		# {"feature": "Bar", "instances": 25, "metric_value": 0.971, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Time", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[12]>1:
								# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2]>0:
									return 'False'
								elif obj[2]<=0:
									# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[12]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]>0:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=1:
				return 'True'
			elif obj[4]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
