def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=5:
		# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>1.0:
			return 'True'
		else: return 'True'
	elif obj[3]>5:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
