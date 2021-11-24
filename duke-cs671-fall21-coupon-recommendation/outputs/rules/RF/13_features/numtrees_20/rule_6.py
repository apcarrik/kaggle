def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[10]>0.0:
		# {"feature": "Age", "instances": 45, "metric_value": 0.9911, "depth": 2}
		if obj[4]>1:
			# {"feature": "Education", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Time", "instances": 24, "metric_value": 0.995, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Gender", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[7]>5:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[12]<=2:
								return 'True'
							elif obj[12]>2:
								return 'False'
							else: return 'False'
						elif obj[7]<=5:
							return 'False'
						else: return 'False'
					elif obj[3]>0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[12]<=2:
							return 'False'
						elif obj[12]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>1:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=17:
				# {"feature": "Bar", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[12]>1:
						# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]>1:
								return 'True'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[12]<=1:
						return 'True'
					else: return 'True'
				elif obj[8]>1.0:
					return 'True'
				else: return 'True'
			elif obj[7]>17:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]<=0.0:
		return 'True'
	else: return 'True'
