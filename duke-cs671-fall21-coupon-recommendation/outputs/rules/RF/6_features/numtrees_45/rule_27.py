def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[3]<=19:
			# {"feature": "Passanger", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Distance", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[5]>1:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>-1.0:
						return 'False'
					elif obj[4]<=-1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>19:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
