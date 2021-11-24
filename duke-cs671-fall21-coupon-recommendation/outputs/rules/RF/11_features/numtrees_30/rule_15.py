def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 23, "metric_value": 0.6666, "depth": 2}
		if obj[4]>1:
			# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[3]<=4:
					return 'True'
				elif obj[3]>4:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>2:
						return 'True'
					elif obj[0]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>1.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[9]<=0:
				return 'False'
			elif obj[9]>0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
