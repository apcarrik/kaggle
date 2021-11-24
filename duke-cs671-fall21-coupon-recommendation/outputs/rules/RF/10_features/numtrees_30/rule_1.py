def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.994, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[8]<=0:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[0]>1:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>3:
							return 'True'
						elif obj[3]<=3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=0.0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=0:
							return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					elif obj[7]>0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[8]>0:
				return 'True'
			else: return 'True'
		elif obj[6]>1.0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[4]>0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[9]<=2:
					return 'False'
				elif obj[9]>2:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[2]>2:
			return 'True'
		elif obj[2]<=2:
			# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[7]<=1.0:
					return 'False'
				elif obj[7]>1.0:
					return 'True'
				else: return 'True'
			elif obj[6]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
