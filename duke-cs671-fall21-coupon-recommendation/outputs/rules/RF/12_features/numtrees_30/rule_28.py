def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>0:
		# {"feature": "Gender", "instances": 29, "metric_value": 0.8498, "depth": 2}
		if obj[3]<=0:
			# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[8]>0.0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=12:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=1.0:
							return 'True'
						elif obj[7]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>12:
					return 'False'
				else: return 'False'
			elif obj[8]<=0.0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]<=18:
					return 'False'
				elif obj[6]>18:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>0:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[7]<=1.0:
				return 'True'
			elif obj[7]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
