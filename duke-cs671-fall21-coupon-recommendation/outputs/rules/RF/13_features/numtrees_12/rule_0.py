def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Age", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[4]>1:
		# {"feature": "Education", "instances": 58, "metric_value": 0.9444, "depth": 2}
		if obj[6]<=1:
			# {"feature": "Occupation", "instances": 32, "metric_value": 0.9972, "depth": 3}
			if obj[7]<=10:
				# {"feature": "Passanger", "instances": 27, "metric_value": 0.951, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>1.0:
							# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=2:
								return 'False'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]>1.0:
						# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=0.0:
							return 'False'
						elif obj[8]>0.0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[7]>10:
				return 'False'
			else: return 'False'
		elif obj[6]>1:
			# {"feature": "Occupation", "instances": 26, "metric_value": 0.6194, "depth": 3}
			if obj[7]<=11:
				# {"feature": "Bar", "instances": 22, "metric_value": 0.4395, "depth": 4}
				if obj[8]<=0.0:
					return 'False'
				elif obj[8]>0.0:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[9]<=2.0:
									return 'True'
								elif obj[9]>2.0:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					elif obj[10]>1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[7]>11:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]>2:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[12]>1:
							return 'True'
						elif obj[12]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[4]<=1:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.8767, "depth": 2}
		if obj[7]<=6:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[6]>0:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[0]>1:
					# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=0:
							return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[7]>6:
			return 'True'
		else: return 'True'
	else: return 'True'
