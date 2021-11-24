def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[4]>0:
		# {"feature": "Occupation", "instances": 44, "metric_value": 0.9024, "depth": 2}
		if obj[6]>1:
			# {"feature": "Bar", "instances": 33, "metric_value": 0.9834, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[5]>0:
					# {"feature": "Passanger", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[8]<=2.0:
									return 'True'
								elif obj[8]>2.0:
									return 'False'
								else: return 'False'
							elif obj[9]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								return 'True'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]>1.0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[2]>2:
					return 'True'
				elif obj[2]<=2:
					# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[10]>0:
						return 'True'
					elif obj[10]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[6]<=1:
			return 'True'
		else: return 'True'
	elif obj[4]<=0:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
