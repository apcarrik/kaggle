def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[3]<=12:
		# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]>1:
							return 'True'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[6]>0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[3]>12:
		return 'False'
	else: return 'False'
