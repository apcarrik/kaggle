def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 33, "metric_value": 0.799, "depth": 2}
		if obj[3]<=1:
			return 'True'
		elif obj[3]>1:
			# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[8]<=0:
				# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[6]<=3.0:
						return 'False'
					elif obj[6]>3.0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=6:
							return 'True'
						elif obj[4]>6:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=7:
						return 'True'
					elif obj[4]>7:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]>1.0:
					return 'False'
				elif obj[7]<=1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>1.0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[1]>0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=6:
							return 'False'
						elif obj[4]>6:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
