def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[6]>0.0:
		# {"feature": "Time", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[7]>1.0:
				return 'True'
			elif obj[7]<=1.0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]>1:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>2:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=2:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[7]>2.0:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[10]<=1:
					return 'False'
				elif obj[10]>1:
					return 'True'
				else: return 'True'
			elif obj[7]<=2.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[6]<=0.0:
		# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[10]>1:
					return 'True'
				elif obj[10]<=1:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
