def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Direction_same", "instances": 34, "metric_value": 0.7871, "depth": 1}
	if obj[8]<=0:
		# {"feature": "Bar", "instances": 26, "metric_value": 0.6194, "depth": 2}
		if obj[5]>0.0:
			return 'True'
		elif obj[5]<=0.0:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[6]>0.0:
					return 'True'
				elif obj[6]<=0.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[9]<=2:
								return 'False'
							elif obj[9]>2:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>0:
		# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 2}
		if obj[3]>0:
			# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[6]>2.0:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]>0.0:
					return 'False'
				elif obj[7]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[6]<=2.0:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
