def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]>0:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9932, "depth": 2}
		if obj[1]>1:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[4]>-1.0:
				# {"feature": "Education", "instances": 22, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=-1.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1.0:
						return 'False'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=0:
		return 'True'
	else: return 'True'
