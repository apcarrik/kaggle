def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[3]<=13:
			# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>2:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>13:
			return 'False'
		else: return 'False'
	elif obj[4]>1.0:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[3]>1:
			return 'False'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
