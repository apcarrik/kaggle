def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[10]>1:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[5]>5:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[2]>0:
				# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]>1.0:
						return 'True'
					elif obj[8]<=1.0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=4:
						return 'False'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[5]<=5:
			return 'True'
		else: return 'True'
	elif obj[10]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[4]>0:
			return 'False'
		elif obj[4]<=0:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[6]<=2.0:
				return 'True'
			elif obj[6]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
