def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[10]<=2:
		# {"feature": "Education", "instances": 39, "metric_value": 0.7793, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.5917, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]>4:
							return 'True'
						elif obj[5]<=4:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[7]>1.0:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[5]>4:
					return 'False'
				elif obj[5]<=4:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]>2:
		# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[4]>0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[5]>1:
				return 'False'
			elif obj[5]<=1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
