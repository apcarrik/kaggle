def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[3]>0:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=6:
							return 'True'
						elif obj[5]>6:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]>1.0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=6:
							return 'True'
						elif obj[5]>6:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[7]>1.0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[7]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
