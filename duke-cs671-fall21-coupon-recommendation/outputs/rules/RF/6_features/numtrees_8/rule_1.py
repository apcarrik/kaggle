def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 99, "metric_value": 0.9911, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Occupation", "instances": 79, "metric_value": 0.9999, "depth": 3}
			if obj[3]>0:
				# {"feature": "Education", "instances": 76, "metric_value": 0.9995, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Coupon", "instances": 74, "metric_value": 0.9979, "depth": 5}
					if obj[1]>1:
						# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.998, "depth": 6}
						if obj[4]<=2.0:
							return 'True'
						elif obj[4]>2.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[5]>2:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[3]>7:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 28, "metric_value": 0.6769, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.5294, "depth": 3}
			if obj[3]<=4:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[1]>0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]>4:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]>-1.0:
				return 'False'
			elif obj[4]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
