def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 58, "metric_value": 0.9444, "depth": 2}
		if obj[7]>2:
			# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.8454, "depth": 3}
			if obj[10]<=2.0:
				# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 4}
				if obj[2]>0:
					# {"feature": "Bar", "instances": 26, "metric_value": 0.9957, "depth": 5}
					if obj[9]>0.0:
						# {"feature": "Direction_same", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[12]<=0:
							# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[4]>1:
								return 'False'
							elif obj[4]<=1:
								# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0:
									return 'True'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[12]>0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]<=0.0:
						# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=2:
							return 'True'
						elif obj[4]>2:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]<=6:
									return 'False'
								elif obj[8]>6:
									return 'True'
								else: return 'True'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]>2.0:
				return 'False'
			else: return 'False'
		elif obj[7]<=2:
			# {"feature": "Children", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[9]<=2.0:
						return 'False'
					elif obj[9]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 27, "metric_value": 0.7642, "depth": 2}
		if obj[6]>0:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[13]>1:
					return 'True'
				elif obj[13]<=1:
					# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[11]<=1.0:
							return 'False'
						elif obj[11]>1.0:
							return 'True'
						else: return 'True'
					elif obj[4]>3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[6]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
