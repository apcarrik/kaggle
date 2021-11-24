def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[11]>1:
		# {"feature": "Time", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[6]<=14:
				# {"feature": "Passanger", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[7]>1.0:
						# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					elif obj[7]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[6]>14:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[11]<=1:
		return 'True'
	else: return 'True'
