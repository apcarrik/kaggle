def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[6]<=7:
		# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 2}
		if obj[2]>2:
			# {"feature": "Direction_same", "instances": 22, "metric_value": 0.7732, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Bar", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=1:
									return 'False'
								elif obj[5]>1:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[7]>1.0:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=2.0:
						return 'False'
					elif obj[8]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>0:
				return 'True'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]>1:
					# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1:
								return 'False'
							elif obj[4]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[11]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>7:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[8]>0.0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=0.0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[5]>1:
					return 'True'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]>2.0:
			return 'False'
		else: return 'False'
	else: return 'False'
