def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]<=0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>2:
							return 'False'
						elif obj[3]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[7]>0:
		return 'False'
	else: return 'False'
