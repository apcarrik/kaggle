def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]>1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[3]<=17:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[1]>2:
				# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[0]>1:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>2:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		elif obj[3]>17:
			return 'False'
		else: return 'False'
	elif obj[5]<=1:
		return 'False'
	else: return 'False'
