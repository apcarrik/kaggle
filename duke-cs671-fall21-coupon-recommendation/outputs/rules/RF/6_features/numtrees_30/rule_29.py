def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.9403, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Coupon", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[5]>1:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>12:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
