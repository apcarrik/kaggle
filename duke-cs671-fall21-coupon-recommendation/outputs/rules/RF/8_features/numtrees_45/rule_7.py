def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[3]<=5:
					# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[6]<=0:
						return 'True'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[3]>5:
					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=0:
						return 'False'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]>2:
		return 'False'
	else: return 'False'
