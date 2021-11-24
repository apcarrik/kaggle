def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9306, "depth": 2}
		if obj[4]<=7:
			# {"feature": "Time", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[6]>1.0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[9]<=2:
						return 'True'
					elif obj[9]>2:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=2:
							return 'True'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=1.0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0.0:
						return 'False'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[4]>7:
			# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[3]<=2:
				return 'False'
			elif obj[3]>2:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
